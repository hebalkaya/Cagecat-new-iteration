'''
The following is the code required to run cblaster

# Creating the DIAMOND database
cblaster makedb [.txt file containing .gbk file locations] -n [database name]

# Searching against the .dmnd database
cblaster search -m local -db [.dmnd database file] -qf [.gbk query file] -o summary.csv -s session.json



To give an example, following code was used for the Leiden demonstration:
Querying BGC0002016 from MIBiG against the Streptomyces_complete database

# Creating the DIAMOND database
cblaster makedb /lustre/BIF/nobackup/balka001/Databases/Streptomyces_complete/Streptomyces_complete_allgbff_files.txt -n Streptomyces_complete

# Searching against the Streptomyces_complete.dmnd database
cblaster search -m local -db /lustre/BIF/nobackup/balka001/Databases/Streptomyces_complete/Streptomyces_complete.dmnd -qf /lustre/BIF/nobackup/balka001/LeidenDemo/BGC0002016.gb -b binary.txt -o summary.csv -s session.json
'''