import os, pprint

class Build:

  def __init__(self, commands = {}, pjkt_folders = []):
    self.commands = commands
    self.pjkt_folders = pjkt_folders
    

  def create(self):
    try:
      os.mkdir(self.commands['destination']+'/'+self.commands['name'])
      
      for folder in self.pjkt_folders:
        os.mkdir(self.commands['destination']+'/'+self.commands['name']+folder)

      command_list = [l for l in self.commands]
      # project_foldders = [path for path in self.pjkt_folders]
      pprint.pprint("This is the list of all commands" + str(command_list))
    except:
      print("[Error]: An error occured when trying to create the workspace folder")

  def create_files(self, file_name):
    new_file = open(file_name, 'w')
    
    try:
      if new_file.writable:
        # TODO: write to file
        new_file.writelines()
      else:
        new_file.close()
    except:
      new_file.close()
      print("[Write Error] An error occured while trying to write to the file")

    new_file.close()