import ase



class Layer:
    """
    Layer是tds中的一个结构，用于储存一层的信息，他也是一个文件，后缀名为 .layer
    """
    def __init__(self):
        self.atom_type = []
        self.atom_num = []
        self.pos = []
        self.force = []
        pass
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
class TDS:
    """
    Two-dimensional surface structure(TDSS)是用于构建二维层状结构的通用文件格式,仅包含二维信息,不需要三维信息
    """

    def __init__(self, file):
        pass
    
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
        self.layers = []
        self.name = None
        pass
        