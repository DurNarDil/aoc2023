input='''seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4'''

class Almanac:
    def __init__(self, input) -> None:
        self.lineList = input.split("\n")
        self.sections = input.split('\n\n')
        self.seeds = self.getSeeds()
        self.seedSoilList = self.getValues(1)
        self.soilFertList = self.getValues(2)
        self.fertWaterList = self.getValues(3)
        self.waterLightList = self.getValues(4)
        self.lightTempList = self.getValues(5)
        self.tempHumidList = self.getValues(6)
        self.humidLocList = self.getValues(7)
        self.soil = []
        self.water = []
        self.fert = []
        self.light = []
        self.temp = []
        self.humid = []
        self.loc = []

        
    def getSeeds(self) -> list:
        split = self.sections[0].split(':')[1]
        return split.split()
        
    def getValues(self, section: int) -> list:
        split = self.sections[section].split(':')[1]
        lineSplit = split.strip().split('\n')
        return lineSplit
    
    def getMappedValue(self, inputList: list, inputInt: int) -> int:
        for map in inputList:
            map = map.split()
            if int(map[1]) <= inputInt and (int(map[1]) + int(map[2])) >= inputInt:
                return inputInt - int(map[1]) + int(map[0])
        return inputInt
    
    def processRanges(self) -> int:
        for index,seed in enumerate(self.seeds):
            self.soil.append(self.getMappedValue(self.seedSoilList, int(seed)))
            self.fert.append(self.getMappedValue(self.soilFertList, int(self.soil[index])))
            self.water.append(self.getMappedValue(self.fertWaterList, int(self.fert[index])))
            self.light.append(self.getMappedValue(self.waterLightList, int(self.water[index])))
            self.temp.append(self.getMappedValue(self.lightTempList, int(self.light[index])))
            self.humid.append(self.getMappedValue(self.tempHumidList, int(self.temp[index])))
            self.loc.append(self.getMappedValue(self.humidLocList, int(self.humid[index])))
        return min(self.loc)
        
        
            
    # def recursive(self) -> list:
    #     input = self.seeds
    #     for int in input:
    #         output.append()



