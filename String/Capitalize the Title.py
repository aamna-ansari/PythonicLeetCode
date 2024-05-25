class Solution:
    def capitalizeTitle(self, title: str) -> str:
        str = ""
        x = title.split()

        for i in x:
            if len(i) > 2:
                str = str + i.title() + ' '
            else: 
                 str = str + i.lower() + ' '
        return str.rstrip()