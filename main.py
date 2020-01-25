# import torch
# import torchvision
# from torchvision import datasets, transforms
import cityscapes_downloader

# # TODO: Remove this after testing
# train_set = datasets.Cityscapes(
#     root='./resources/datasets/cityscapes/',
#     split='train',
#     mode='fine',
#     transform=transforms.Compose([
#         transforms.ToTensor()
#     ])
# )


def main():
    # TODO: Create an aimas-wide cityscapes user
    csd = cityscapes_downloader.CityscapesDownloader(
        root='./resources/datasests/cityscapes/',
        login={'user': 'None', 'pass': 'None'},
        packages=['gtFine', 'gtCoarse', 'leftImg8bit']
    )

    csd.download()
    return


if __name__ == '__main__':
    main()
