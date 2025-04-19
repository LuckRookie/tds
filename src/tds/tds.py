import array
import ase
import numpy as np
from typing import List,Union


class Layer:
    """
    Layer是tds的其中一个结构，用于储存一层的信息，他也是一个文件，后缀名为 .layer
    """
    def __init__(
        self,
        atom_type:List[str] = [],    # 元素种类 [C,N,O]
        atom_num:List[int] = [],     # 元素个数 [1,2,3]
        pos:List[List[float]] = [],  # 原子坐标 [[x,y,z],[x,y,z],[x,y,z]]
        span:float = 0.0             # 与下一层的距离
    ):

        self.atom_type = atom_type
        self.atom_num = atom_num
        self.pos = pos
        self.span = span
        self.check()

    def check(self):
        """
        检查Layer的信息是否正确
        """
        if len(self.atom_type) != len(self.atom_num):
            raise ValueError("atom_type and atom_num must have the same length")
        if len(self.pos) != sum(self.atom_num):
            raise ValueError("pos and atom_num must have the same length")
        if self.span < 0:
            raise ValueError("span must be positive")

    def parse_file(self,file):
        '''
        Layer # 层
        C N Ti #元素类型
        x x x  # 对应的元素个数
        Position # 原子坐标(笛卡尔坐标),分数坐标没办法表征二维中的上下的相对位置
        C x x x
        C x x x # 这里不省略元素种类，是为了给缺陷原子做准备
        N x x x
            .
            .
            .
        Span # 与下一层之间的距离,没有就为0A
        15
        ---- # layer文件最后一定要有----
        '''
        pass

    def write_file(self, file):
        """将Layer对象的数据写入文件
        Args:
            file: 文件路径或文件对象
        """
        if isinstance(file, str):
            f = open(file, 'w')
        else:
            f = file

        with f:
            # 写入Layer标记
            f.write("Layer\n")

            # 写入元素类型
            f.write(" ".join(self.atom_type) + "\n")

            # 写入元素个数
            f.write(" ".join(map(str, self.atom_num)) + "\n")

            # 写入Position标记和原子坐标
            f.write("Position\n")
            for i, pos in enumerate(self.pos):
                # 获取当前原子对应的元素类型
                atom_index = 0
                count = 0
                for j, num in enumerate(self.atom_num):
                    count += num
                    if i < count:
                        atom_index = j
                        break
                # 写入原子类型和坐标
                f.write(f"{self.atom_type[atom_index]} {' '.join(map(str, pos))}\n")

            # 写入Span和距离值
            f.write("Span\n")
            f.write(f"{self.span}\n")

            # 写入结束标记
            f.write("----\n")

class TDS:
    """
    Two-dimensional surface structure(TDSS)是用于构建二维层状结构的通用文件格式,仅包含二维信息,不需要三维信息
    因为没有Z轴坐标，因此在构建三维结构的时候，z轴一定与xy平面垂直
    """

    def __init__(
        self,
        name:str = "TDS",
        layers:List[Layer] = [],
        vector:Union[List[List[float]], np.ndarray] = []
    ):
        self.name:str = name
        self.layers:List[Layer] = layers
        self.vector:Union[List[List[float]], np.ndarray] = vector

    def parse_file(self,file):
        '''
        文件的后缀名为.tds

        [NAME] # name of the structure
        xxxx
        Base Vector # 二维的基向量
        x x
        x x
        ----
        Layer # 层
        C N Ti #元素类型
        x x x  # 对应的元素个数
        Position # 原子坐标(笛卡尔坐标),分数坐标没办法表征二维中的上下的相对位置
        C x x x
        C x x x # 这里不省略元素种类，是为了给缺陷原子做准备
        N x x x
            .
            .
            .
        Span # 与下一层之间的距离,没有就为0A
        15
        ----
        Layer # 层，下一层的元素的Z坐标也是从0开始
        ......

        '''
        pass
