__version__ = "1.0.0"


from . import utils_callback
from . import utils_gen
from . import utils_imgproc
from . import utils_loss
from . import wnet


def get_data_path():
    import os

    return os.environ["PYTHON_ENV"] + "/data/paths_train_val_test"
