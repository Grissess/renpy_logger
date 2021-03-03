import sys, os, time, atexit

import renpy

renpy.config.log_to_stdout = True

# We're probably running in Py2, well before the stdlin contained convenient IO
# redirection primitives, so...

class Teed(object):
    def __init__(self, *streams):
        self.streams = streams

    def __getattr__(self, attr):
        return getattr(self.streams[0], attr)

    # Special cases follow

    def write(self, data):
        res = None
        for st in self.streams:
            ret = st.write(data)
            if res is None:
                res = ret
        return ret

    def flush(self):
        for st in self.streams:
            st.flush()

    def close(self):
        for st in self.streams:
            st.close()

# basepath is init'd just before RPEs are executed
try:
    log_path = os.path.join(renpy.game.basepath, 'output.txt')
    if os.path.exists(log_path):
        # Rotate into output.0.txt, output.1.txt, output.2.txt, ...
        # The newest log is always output.txt; the second newest has the
        # _highest_ number, the third newest the next highest, etc.
        for i in range(100):
            new_path = os.path.join(renpy.game.basepath, 'output.%d.txt' % (i,))
            if not os.path.exists(new_path):
                os.rename(log_path, new_path)
                break
        else:
            os.unlink(log_path)
except Exception:
    import traceback
    traceback.print_exc()
    print('Above exception while trying to rotate logs--dazed but continuing...')

fl = open(os.path.join(renpy.game.basepath, 'output.txt'), 'w')
fl.write('--- Ren\'Py Logger started on %s ---\n' % (time.ctime(),))

sys.stdout = Teed(sys.stdout, fl)
sys.stderr = Teed(sys.stderr, fl)

sys.stdout.write('1: Test stdout\n')
sys.stderr.write('2: Test stderr\n')
print('3: Test print')
fl.write("(If you don't see three tests above this line, check your installation.)\n")

@atexit.register
def _flush_logs():
    fl.write('\n- Log ending (process exiting) -\n')
    fl.flush()
