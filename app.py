from vetiver import VetiverModel
import vetiver
import pins
import logging
import os 
   
# Get the path of current working directory 
path = os.getcwd() 
   
# Get the list of all files and directories 
dir_list = os.listdir(path)

logging.warning(dir_list)


b = pins.board_folder('./data/model', allow_pickle_read=True)
v = VetiverModel.from_pin(b, 'penguin_model')

vetiver_api = vetiver.VetiverAPI(v)
api = vetiver_api.app
