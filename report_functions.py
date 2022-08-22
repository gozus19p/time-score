import os


def prepare_archive(archive_name, subdirectory_name):
    # Clearing the history of the day before
    archive_subdirectories = os.listdir('archive')
    create_archive = not archive_subdirectories.__contains__(archive_name)

    # Creating directory if needed
    if create_archive:
        print(f'Creating archive archive for the month {archive_name}...')
        os.mkdir(f'archive/{archive_name}')

    create_sub_archive = not os.listdir(f'archive/{archive_name}').__contains__(subdirectory_name)

    if create_sub_archive:
        print(f'Creating archive directory for the day {subdirectory_name}...')
        os.mkdir(f'archive/{archive_name}/{subdirectory_name}')
