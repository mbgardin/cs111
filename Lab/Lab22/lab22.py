import matplotlib
matplotlib.use('Agg')  # Ensure compatibility for environments without display servers
import matplotlib.pyplot as plt
import csv

def plot_histogram():
    gpas, sats = [], []

    with open('admission_algorithms_dataset.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            sats.append(float(row[1]))
            gpas.append(float(row[2]))

    # GPA Histogram
    plt.figure(figsize=(6.4, 4.8), dpi=100)
    plt.hist(gpas, bins=10)
    plt.savefig("gpa.png", format='png')
    plt.clf()

    # SAT Histogram
    plt.figure(figsize=(6.4, 4.8), dpi=100)
    plt.hist(sats, bins=10)
    plt.savefig("sat_score.png", format='png')
    plt.clf()

def plot_scatter():
    gpas, sats = [], []

    with open('admission_algorithms_dataset.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            sats.append(float(row[1]))
            gpas.append(float(row[2]))

    plt.figure(figsize=(6.4, 4.8), dpi=100)
    plt.scatter(gpas, sats)
    plt.savefig("correlation.png", format='png')
    plt.clf()

def plot_spectra():
    wavelength1, flux1 = [], []
    wavelength2, flux2 = [], []

    with open("spectrum1.txt", "r") as file1, open("spectrum2.txt", "r") as file2:
        for line in file1:
            w, f = map(float, line.split())
            wavelength1.append(w)
            flux1.append(f)
        for line in file2:
            w, f = map(float, line.split())
            wavelength2.append(w)
            flux2.append(f)

    plt.figure(figsize=(6.4, 4.8), dpi=100, facecolor='white')
    plt.plot(wavelength1, flux1, color='blue', linewidth=1.5)
    plt.plot(wavelength2, flux2, color='green', linewidth=1.5)
    plt.savefig("spectra.png", format='png', facecolor='white')
    plt.clf()

def main():
    plot_histogram()
    plot_scatter()
    plot_spectra()

if __name__ == "__main__":
    main()
