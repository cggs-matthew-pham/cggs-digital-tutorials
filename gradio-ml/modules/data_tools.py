from pathlib import Path

import random
import shutil
import urllib.request
import zipfile


def dataset_summary(folder):
    """
    Show the number of files in each class folder.
    """

    folder = Path(folder)

    print(f"\nDataset: {folder}\n")

    total = 0

    for class_folder in sorted(folder.iterdir()):

        if not class_folder.is_dir():
            continue

        files = [
            file
            for file in class_folder.iterdir()
            if file.is_file()
        ]

        print(
            f"{class_folder.name}: "
            f"{len(files)} examples"
        )

        total += len(files)

    print(f"\nTotal: {total} examples")


def make_subset(
    source,
    destination,
    classes=None,
    samples_per_class=100,
    seed=42
):
    """
    Create a smaller classroom-friendly dataset.
    """

    source = Path(source)
    destination = Path(destination)

    destination.mkdir(
        parents=True,
        exist_ok=True
    )

    random.seed(seed)

    class_folders = [
        folder
        for folder in source.iterdir()
        if folder.is_dir()
    ]

    if classes is not None:
        class_folders = [
            folder
            for folder in class_folders
            if folder.name in classes
        ]

    for class_folder in class_folders:

        output_folder = (
            destination / class_folder.name
        )

        output_folder.mkdir(
            parents=True,
            exist_ok=True
        )

        files = [
            file
            for file in class_folder.iterdir()
            if file.is_file()
        ]

        random.shuffle(files)

        selected = files[:samples_per_class]

        for file in selected:

            shutil.copy(
                file,
                output_folder / file.name
            )

        print(
            f"{class_folder.name}: "
            f"{len(selected)} files copied"
        )


def download_zip(
    url,
    destination="datasets",
    filename="dataset.zip"
):
    """
    Download and extract a ZIP dataset.
    """

    destination = Path(destination)

    destination.mkdir(
        parents=True,
        exist_ok=True
    )

    zip_path = destination / filename

    print("Downloading dataset...")

    urllib.request.urlretrieve(
        url,
        zip_path
    )

    print("Extracting dataset...")

    with zipfile.ZipFile(
        zip_path,
        "r"
    ) as archive:

        archive.extractall(destination)

    zip_path.unlink()

    print(
        f"Dataset extracted to "
        f"{destination}"
    )

    return destination