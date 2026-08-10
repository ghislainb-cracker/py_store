# ==============================
# INSTALLATION REQUIREMENT
# ==============================

# Required external package:
#
# pip install pytubefix
#
# pytubefix provides tools to communicate
# with YouTube and access video streams





# ==============================
# IMPORT REQUIRED LIBRARIES
# ==============================


# Import YouTube class from pytubefix
#
# This handles:
# - connecting to YouTube
# - retrieving video information
# - accessing available streams
from pytubefix import YouTube



# Import tkinter because we need a graphical
# folder selection window
import tkinter as tk



# Import filedialog because it provides
# the folder picker functionality
from tkinter import filedialog





# ==============================
# VIDEO DOWNLOADING FUNCTION
# ==============================

# Function responsible for downloading a YouTube video
#
# Parameters:
#
# url:
#     YouTube video link provided by user
#
# save_path:
#     Folder where the downloaded file will be stored
def download_video(
    url,
    save_path
):


    # Use try/except because downloading involves
    # external systems:
    #
    # - internet connection problems
    # - invalid URLs
    # - unavailable videos
    # - permission issues
    try:


        # Inform the user that connection has started
        print(
            "Connecting to YouTube..."
        )



        # Create a YouTube object
        #
        # This sends a request to YouTube
        # and loads information about the video
        yt = YouTube(
            url
        )



        # Display video title
        # This confirms that the video was found
        print(
            f"Title: {yt.title}"
        )



        print(
            "Preparing download..."
        )





        # ==============================
        # STREAM SELECTION
        # ==============================


        # YouTube videos have multiple streams:
        #
        # Different:
        # - resolutions
        # - formats
        # - audio/video combinations
        #
        # Filter streams to find:
        #
        # progressive=True:
        #     video and audio already combined
        #
        # file_extension="mp4":
        #     choose MP4 format
        stream = (
            yt.streams
            .filter(
                progressive=True,
                file_extension="mp4"
            )
            .get_highest_resolution()
        )



        # Start downloading the selected stream
        print(
            "Downloading..."
        )



        # Save the video into the selected folder
        stream.download(
            output_path=save_path
        )



        # Notify the user after completion
        print(
            "Video downloaded successfully!"
        )





    # Catch any unexpected error
    except Exception as e:


        # Inform user that download failed
        print(
            "\nDownload failed!"
        )



        # Display the category of error
        #
        # Example:
        # TypeError
        # ConnectionError
        print(
            "Error type:",
            type(e).__name__
        )



        # Display the actual error message
        print(
            "Details:",
            e
        )





# ==============================
# FOLDER SELECTION SYSTEM
# ==============================

# Function responsible for opening
# a graphical folder selection window
#
# Returns:
# Selected folder path
def open_file_dialog():


    # Open folder picker
    #
    # User chooses where the video should be saved
    folder = filedialog.askdirectory()



    # Check whether the user selected a folder
    if folder:


        print(
            f"Selected folder: {folder}"
        )


        # Return selected location
        return folder



    # If user cancels selection,
    # return nothing
    return None





# ==============================
# PROGRAM ENTRY POINT
# ==============================


# Ensures this code only runs
# when this file is executed directly
#
# It prevents automatic execution
# if this file is imported elsewhere
if __name__ == "__main__":



    # Create a Tkinter application window
    root = tk.Tk()



    # Hide the main window
    #
    # We only need the folder picker,
    # not a complete GUI application
    root.withdraw()





    # ==============================
    # USER INPUT
    # ==============================


    # Ask user for YouTube video link
    video_url = input(
        "Please enter a YouTube URL: "
    )



    # Open folder selector
    # and get save location
    save_dir = open_file_dialog()



    # Check whether a folder was selected
    if save_dir:


        # Start downloading process
        download_video(
            video_url,
            save_dir
        )



    # Handle case where user cancels folder selection
    else:

        print(
            "No folder selected. Exiting..."
        )