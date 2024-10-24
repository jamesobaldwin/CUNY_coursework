import numpy as np
import matplotlib.pyplot as plt
from dcst import dct, idct
from numpy.fft import rfft, irfft
import argparse


'''
Pass to the command line a list of the file names and percentages of coefficients 
that you want to visualize. All combinations of files, percentages, and cosine/discrete
transforms will be calculated and plotted on a single graph

eg: python CM_hw5_baldwin.py dow.txt dow2.txt --keep_fraction 0.2 0.1 0.03 0.01
'''


def parse_arguments():
    parser = argparse.ArgumentParser(description="Process some inputs.")
    parser.add_argument(
        "filenames", 
        type=str, 
        nargs='+',
        help="Input filenames (required).")
    parser.add_argument(
        "--keep_fractions",
        type=float,
        nargs='+',  # Allows multiple values for keep_fraction
        default=[0.1],
        help="List of percentages (as float) of coefficients in FFT to retain. Provide space-separated values.",
    )
    parser.add_argument(
        "--cosine",
        action="store_true",
        default=False,
        help="When True, uses Discrete Cosine Transform. When False (default) uses Discrete FT.",
    )
    parser.add_argument(
        "--save_plot", 
        type=str, 
        default=False, 
        help="When True, final plot will be saved to root directory (default False)."
    )
    return parser.parse_args()


def sparse_inverse(filename, keep_fraction: float = 0.1, cosine: bool = False):
    # read in the data
    y = np.loadtxt(filename)
    # set trasnform and inverse to be either DFT or DCT
    if cosine:
        fft = dct
        ifft = idct
        transform_type = "Cosine Transform"
    else:
        fft = rfft
        ifft = irfft
        transform_type = "Discrete Transform"

    c = fft(y)
    cutoff = int(len(c) * keep_fraction)
    c[cutoff:] = 0
    f_sparse = ifft(c)

    return y, f_sparse, transform_type

def plot_transformed_data(ax, y, f, filename, transform_type, keep_fraction):
    ax.plot(y, color="blue", label="original data", lw=2, alpha=0.4)
    ax.plot(f, color="red", label="inverse sparse FT")
    ax.set_title(f"{filename} {transform_type} ({keep_fraction*100}%)")
    ax.legend()

if __name__ == "__main__":
    args = parse_arguments()

    # Calculate the number of subplots needed
    num_plots = len(args.filenames) * 2 * len(args.keep_fractions)
    num_rows = int(np.ceil(np.sqrt(num_plots)))
    num_cols = int(np.ceil(num_plots / num_rows))

    # Create subplots grid
    fig, axs = plt.subplots(num_rows, num_cols, figsize=(15, 10), sharex=True, sharey=True)
    axs = axs.flatten()  # Flatten in case of multiple rows/columns

    plot_idx = 0

    # Loop over both the cosine = True and cosine = False cases
    for file in args.filenames:
        for cosine in [True, False]:
            for keep_fraction in args.keep_fractions:
                print(f"Running with cosine={cosine}, keep_fraction={keep_fraction}")
                y, f, type = sparse_inverse(file, keep_fraction=keep_fraction, cosine=cosine)
                plot_transformed_data(axs[plot_idx], y, f, file, type, keep_fraction)
                plot_idx += 1

    # Adjust layout and show the plot
    plt.tight_layout()
    if args.save_plot:
        plt.savefig('dow_transforms.png')
    plt.show()

