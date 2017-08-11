import sys

from sat_reader_kaldi import SatReaderKaldi
from utils.fileutils import debug


#it returns an object reader that internaly will manage all the data
#client will be agnostic for the internals
#TODO we need to create a separate sat reader
def create_reader(info_format, config, batches_id = None):

    #sanity check for feats
    #read features with kaldi format
    if info_format == "kaldi": return SatReaderKaldi(config, batches_id)

    else:
        print("Error: "+info_format+" is not defined as \"info_format\" in sat: ")
        print(debug.get_debug_info())
        print("exiting...")
        sys.exit()
