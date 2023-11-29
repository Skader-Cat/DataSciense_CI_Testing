import matplotlib.pyplot as plt
import seaborn as sns

def heatmap_builder(data, title, save_path = None, show = True, figsize=(10, 10), annot=False, fmt='.2g',
                    cmap='viridis', cbar=False, yticklabels = False, xticklabels = False, square = False):
    """
    Создание тепловой карты

    Параметры:
    ----------
    data: array-like
        Данные для построения тепловой карты
    title: str
        Название тепловой карты
    save: bool
        Сохранить тепловую карту
    save_path: str
        Путь сохранения тепловой карты
    figsize: tuple
        Размер тепловой карты
    annot: bool
        Показывать значения в ячейках
    fmt: str
        Формат значений в ячейках
    cmap: str
        Цветовая схема
    cbar: bool
        Показывать цветовую шкалу
    """

    plt.figure(figsize=figsize)
    sns.heatmap(data, annot=annot, fmt=fmt, cmap=cmap, cbar=cbar, yticklabels = yticklabels, xticklabels = xticklabels, square = square)
    plt.title(title)
    if save_path is not None:
        plt.savefig(save_path, bbox_inches='tight')
    if show:
        plt.show()
    plt.close()