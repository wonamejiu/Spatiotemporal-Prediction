from torch.utils.data import DataLoader

from nn.ConvLSTM import ConvLSTM_MovingMNIST, ConvLSTM_KTH, ConvLSTM_TaxiBJ
from utils.data import MovingMNISTDataset, TaxiBJDataset, KTHDataset
from utils.trainer import Trainer


def train_ConvLSTM_Moving_MNIST():
    convlstm = ConvLSTM_MovingMNIST(in_channels=16, hidden_channels_list=[128, 64, 64], size=(16, 16),
                                    kernel_size_list=[5, 5, 5])
    train_set = MovingMNISTDataset("train")
    test_set = MovingMNISTDataset("test")
    validation_set = MovingMNISTDataset("validation")
    train_loader = DataLoader(train_set, batch_size=8, shuffle=True)
    test_loader = DataLoader(test_set, batch_size=1)
    validation_loader = DataLoader(validation_set, batch_size=8)
    trainer = Trainer(max_epoch=1000, device="cuda:0", to_save="results/MovingMNIST/ConvLSTM")
    # trainer.fit(convlstm, train_loader, validation_loader)

    trainer.predict(convlstm, test_loader=test_loader,
                    ckpt_path="results/MovingMNIST/ConvLSTM/checkpoint_000020_0.0200864142_temp.pth")


def train_ConvLSTM_KTH():
    convlstm = ConvLSTM_KTH(in_channels=16, hidden_channels_list=[128, 64, 64], size=(32, 32),
                            kernel_size_list=[5, 5, 5])
    train_set = KTHDataset("train")
    test_set = KTHDataset("test")
    validation_set = KTHDataset("validation")
    train_loader = DataLoader(train_set, batch_size=8, shuffle=True)
    test_loader = DataLoader(test_set, batch_size=1)
    validation_loader = DataLoader(validation_set, batch_size=8)
    trainer = Trainer(max_epoch=1000, device="cuda:0", to_save="results/KTH/ConvLSTM")
    # trainer.fit(convlstm, train_loader, validation_loader)

    trainer.predict(convlstm, test_loader=test_loader,
                    ckpt_path="results/KTH/ConvLSTM/checkpoint_000007_0.0025517840_temp.pth")


def train_ConvLSTM_TaxiBJ():
    convlstm = ConvLSTM_TaxiBJ(in_channels=2, hidden_channels_list=[128, 64, 64], size=(32, 32),
                               kernel_size_list=[5, 5, 5])
    train_set = TaxiBJDataset("train")
    test_set = TaxiBJDataset("test")
    validation_set = TaxiBJDataset("validation")
    train_loader = DataLoader(train_set, batch_size=32, shuffle=True)
    test_loader = DataLoader(test_set, batch_size=1)
    validation_loader = DataLoader(validation_set, batch_size=32)
    trainer = Trainer(max_epoch=1000, device="cuda:0", to_save="results/TaxiBJ/ConvLSTM")
    trainer.fit(convlstm, train_loader, validation_loader)

    # trainer.predict(convlstm, test_loader=test_loader,
    #                 ckpt_path="")


if __name__ == '__main__':
    train_ConvLSTM_TaxiBJ()
