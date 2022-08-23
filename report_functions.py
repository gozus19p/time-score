import os


def prepare_archive(archive_name, subdirectory_name):
    """
    Prepara le directory utili alla creazione dell'archivio.
    :param archive_name: è il nome dell'archivio, inteso come livello più basso di directory
    :param subdirectory_name: è il nome della sotto-directory dell'archivio
    """
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
