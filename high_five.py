class Solution(object):
    def highFive(self, items):
        """
        :type items: List[List[int]]
        :rtype: List[List[int]]
        """
        studentDictionary = dict()
        for item in items:
            temp = studentDictionary.get(item[0])
            if temp == None:
                studentDictionary[item[0]].append(item[1])
            else:
                studentDictionary[item[0]] = temp.append(item[1])
            
        print(studentDictionary)

p = Solution()            
items = [[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100]]
p.highFive(items)