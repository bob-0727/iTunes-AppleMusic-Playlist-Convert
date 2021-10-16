# This script is meant to help users convert the directories in m3u files to thier operating system

# Script by Robert S.
# Made on October 16, 2021
# Help from https://www.geeksforgeeks.org/how-to-search-and-replace-text-in-a-file-in-python/

# defining find and replace variables
# search is the file path of your songs on the starting OS
# replace is the file path of your songs on the end OS
# name is the name of the playlist you are converting
search = "/Users/rbs/Music/Music/Media.localized/Music"
replace = "/home/robert/Music"
name = input("Enter the playlist name: ")

# function to replace the dirs
# credit to https://www.geeksforgeeks.org/how-to-search-and-replace-text-in-a-file-in-python/
def file(name):
	with open(name, 'r') as playlist:
		data = playlist.read()
		data = data.replace(search, replace)

	with open(name, 'w') as playlist:
		playlist.write(data)
		
# run the function and signal that the operation is complete
file(name)
print("Operation complete!")
