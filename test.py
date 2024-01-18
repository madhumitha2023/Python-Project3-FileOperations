def update_server_config(file_path, key, value):
        with open(file_path, "r") as file:
            lines = file.readlines()
            
        with open(file_path, "w") as file:
            for line in lines:
                if key in line:
                    file.write(key + "=" + value + "\n")
                else:
                    file.write(line)

server_config_file = 'server_config.txt'

key_to_update = 'PORT'
new_value = '8000'
            
update_server_config(server_config_file, key_to_update, new_value)