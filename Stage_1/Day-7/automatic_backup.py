# ==============================
# INSTALLATION REQUIREMENT
# ==============================

# Install schedule library:
#
# pip install schedule
#
# This library allows Python programs
# to execute functions at specific times





# ==============================
# IMPORT REQUIRED LIBRARIES
# ==============================


# os provides tools for:
# - creating paths
# - joining folders
# - interacting with the operating system
import os



# shutil provides high-level file operations
#
# We use it to copy entire folders
import shutil



# datetime allows us to create
# date-based backup folder names
import datetime



# schedule allows us to run functions
# automatically at specific times
import schedule



# time allows the program to pause
# between schedule checks
import time





# ==============================
# BACKUP CONFIGURATION
# ==============================


# Folder containing the files we want
# to protect and backup
#
# This is the original location
source_dir = (
    r"C:\Users\VIPER TECH\Pictures\Screenshots"
)



# Folder where backups will be stored
#
# Every backup will be created inside
# this directory
destination_dir = (
    r"C:\Users\VIPER TECH\Desktop\Python Bootcamp\level1\first_vid\Day-7\backups"
)





# ==============================
# BACKUP FUNCTION
# ==============================


# Function responsible for creating
# a copy of the source folder
#
# Parameters:
#
# source:
#     folder that should be copied
#
# dest:
#     location where backup is stored
def copy_folder_to_directory(
    source,
    dest
):


    # Get today's date
    #
    # Example:
    #
    # 2026-08-02
    #
    # This allows every backup to have
    # a unique folder name
    today = datetime.date.today()



    # Create the final backup path
    #
    # Example:
    #
    # backups/
    #     2026-08-02/
    #
    dest_dir = os.path.join(
        dest,
        str(today)
    )





    # Try copying the folder
    try:


        # Copy the entire source folder
        #
        # copytree:
        # - creates destination folder
        # - copies all files/subfolders
        shutil.copytree(
            source,
            dest_dir
        )



        # Inform user after success
        print(
            f"Folder copied to: {dest_dir}"
        )





    # This error happens when:
    #
    # The backup folder already exists
    #
    # Example:
    #
    # Running backup twice on same day
    except FileExistsError:


        print(
            "The destination already exists"
        )





# ==============================
# AUTOMATION SETUP
# ==============================


# Schedule the backup task
#
# This means:
#
# Every day at 13:04:
#     run copy_folder_to_directory()
#
schedule.every().day.at("13:04").do(

    # lambda creates a small anonymous function
    # that calls our backup function
    #
    # It passes the required arguments:
    # source folder
    # destination folder
    lambda:
        copy_folder_to_directory(
            source_dir,
            destination_dir
        )
)





# ==============================
# CONTINUOUS RUNNING LOOP
# ==============================


# The program must keep running
# because it needs to wait for
# the scheduled time
while True:


    # Check if any scheduled task
    # is ready to execute
    schedule.run_pending()



    # Pause for one second
    #
    # Prevents the program from
    # constantly consuming CPU
    time.sleep(1)