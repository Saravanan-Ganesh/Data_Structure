##Gerneral tree
class TreeNode:
    def __init__(self,data):
        self.data=data
        self.children=[]
        self.parent=None

    def add_child(self,child):
        child.parent=self
        self.children.append(child)

    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "-->" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()
                
    def get_level(self):
        level=0
        p=self.parent
        while p:
            level += 1 
            p = p.parent
        return level
        
            
def build_product_tree():
    root=TreeNode("Electronics")
    
    laptop=TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("DELL"))
    laptop.add_child(TreeNode("HP"))
    laptop.add_child(TreeNode("SURFACE"))

    cellphone=TreeNode("Cell phone")
    cellphone.add_child(TreeNode("MI"))
    cellphone.add_child(TreeNode("OPPO"))
    cellphone.add_child(TreeNode("VIVO"))

    tv=TreeNode("tv")
    tv.add_child(TreeNode("LG"))
    tv.add_child(TreeNode("SAMSUNG"))
    tv.add_child(TreeNode("BPL"))

    root.add_child(laptop)
    root.add_child(tv)
    root.add_child(cellphone)

##    print(tv.get_level())
    return root
    
if __name__ == '__main__':
    roo = build_product_tree()
    roo.print_tree()
##    print(roo.get_level())

