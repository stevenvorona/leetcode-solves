class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
    :type grid: List[List[int]]
    :rtype: int
    """
        maxLR = []
        maxUD = []
        def findGreatest(line):
            #line is List
            max = 0
            for i in line:
                if i > max:
                    max = i
            return max
        counter = 0
        for i in grid:
            maxLR.append(findGreatest(i))
            counter += 1
        print maxLR
        switched = []
        counter = 0
        for j in range(0, len(grid[0])):
            switched.append([])
            for i in grid:
                switched[j].append(i[j])

        for i in switched:
            maxUD.append(findGreatest(i))
            counter += 1
        print maxUD

        final = []
        for i in range(0, len(grid)):
            final.append([])
            for j in range(0, len(grid[i])):
                if maxLR[i] >= maxUD[j]:
                    #use maxUD[j]
                    final[i].append(maxUD[j])
                else:
                    final[i].append(maxLR[i])
        print final
        difference = 0
        for i in range(0, len(final)):
            for j in range(0, len(final[i])):
                difference += final[i][j] - grid[i][j]
        return difference
                           
        