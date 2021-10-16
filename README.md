# iTunes-AppleMusic-Playlist-Convert
This script is meant to convert your playlists from iTunes or Apple Music to be compatible with another media player, such as Strawberry on Linux. It changes the directories in the playlists to match where your songs are.

## Important Notes
- I made this script since I couldnt find another that did what I wanted to do reliably. This is my attempt at making that script, and it's not perfect.
- This has only been tested using the Strawberry player on Arch and m3u files generated by Apple Music on Mac.
- When converting to Windows, you would have to change the slashes to the opposite direction.
- Two of my songs failed to convert. I figured out one did not exist at all, but as for the other, I am unsure as to what caused that issue.

## Instructions
1. Edit the python file and change the strings search and replace to match the directories you are changing from and to. Search should be the path of the songs from your starting operating system, replace should be the path you want to change to.
2. Make sure that the script is in a folder/location with the playlists you want to edit, then open the folder in the terminal.
3. Run the program by using the command "python3 convert.py" if you are on linux. If you are on another operating system, then run the script as you normally would on that OS.
4. Enter the name of the playlist you want, including the file extension, and let the script do the rest.
5. Once the operation is complete, I would reccomend going through and checking that everything is converted.
