import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import argparse

def get_descrition():
	description = []
	description.append("")
	description.append("mean frequency (in kHz)")
	description.append("standard deviation of frequency")
	description.append("median frequency (in kHz)")
	description.append("first quantile (in kHz)")
	description.append("third quantile (in kHz)")
	description.append("interquantile range (in kHz)")
	description.append("skewness (see note in specprop description)")
	description.append("kurtosis (see note in specprop description)")
	description.append("spectral entropy")
	description.append("spectral flatness")
	description.append("mode frequency")
	description.append("frequency centroid (see specprop)")
	description.append("average of fundamental frequency measured across acoustic signal")
	description.append("minimum fundamental frequency measured across acoustic signal")
	description.append("Predictor class, male or female")
	description.append("")
	description.append("")
	description.append("")
	description.append("")
	description.append("")
	description.append("")

	return description

def get_data(histogram_id,file):
	index = histogram_id
	columns_index = []
	columns_index.append(index)
	description = get_descrition()
	x = []
	data = pd.read_csv(file, sep=',')
	m = data[(data.label == 1)]
	f = data[(data.label == 0)]
	m_aux = []
	f_aux = []

	for i in range(len(m)):
		y = []
		m_aux.append(m.iloc[i,columns_index[0]])
		f_aux.append(f.iloc[i,columns_index[0]])
		y.append(m.iloc[i,columns_index[0]])
		y.append(f.iloc[i,columns_index[0]])
		x.append(y) 

	columns_name = []
	columns_name.append(data.columns[columns_index[0]])

	return m_aux,f_aux,columns_name[0],description[index]



def plot_histogram(histogram_id,file,file_normalized):

	male_data,female_data,column_name,description = get_data(histogram_id,file)

	plt.subplot(1, 2, 1)
	plt.hist(male_data, 50, alpha=0.5, label='Masculino')
	plt.hist(female_data, 50, alpha=0.5, label='Feminino')
	plt.legend(loc='upper right')
	if description == '':
		plt.title(column_name)
	else:
		plt.title(column_name + " - " + description)
	plt.grid(linestyle='--', alpha=0.5)

	male_data,female_data,column_name,description = get_data(histogram_id,file_normalized)
	plt.subplot(1, 2, 2)
	plt.hist(male_data, 50, alpha=0.5, label='Masculino')
	plt.hist(female_data, 50, alpha=0.5, label='Feminino')
	plt.legend(loc='upper right')
	if description == '':
		plt.title(column_name + " - [normalized]")
	else:
		plt.title(column_name + " - " + description + " - [normalized]")

	plt.grid(linestyle='--', alpha=0.5)

	plt.show()

def main():   
    my_parser = argparse.ArgumentParser()
    my_parser.add_argument('-i', action='store', type=int, required=True, help='Plot histogram, valid values range 0 to 14 ')
    args = my_parser.parse_args()

    if args.i <= 19 and args.i >= 1:
    	plot_histogram(args.i,'dados_voz_genero.csv','normalized_dados_voz_genero.csv')
    else:
    	print("Error: Range value accept 1 to 19")
    	
    
if __name__ == "__main__": 
    main() 




