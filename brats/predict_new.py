import os

from train import config
from unet3d.prediction import run_validation_cases


def main():
    prediction_dir = os.path.abspath("prediction")
    run_validation_cases(validation_keys_file=os.path.abspath("validation_ids.pkl"),
                         model_file=os.path.abspath("isensee_2017_model.h5"),
                         training_modalities=["t1", "t1ce", "flair", "t2"],
                         labels=(1, 2, 4),
                         hdf5_file=os.path.abspath("brats_data.h5"),
                         output_label_map=True,
                         output_dir=prediction_dir)


if __name__ == "__main__":
    main()
