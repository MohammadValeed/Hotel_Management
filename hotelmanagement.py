class Hotel:
    sortParam = 'name'

    def __init__(self):
        self.name = ''
        self.roomAvl = 0
        self.location = ''
        self.rating = 0  # Initialize rating with a value, e.g., 0
        self.pricePr = 0

    def __lt__(self, other):
        return getattr(self, Hotel.sortParam) < getattr(other, Hotel.sortParam)

    @classmethod
    def sortByName(cls):
        cls.sortParam = 'name'

    @classmethod
    def sortByRate(cls):
        cls.sortParam = 'rating'

    @classmethod
    def sortByRoomAvailable(cls):
        cls.sortParam = 'roomAvl'

    def __repr__(self):
        return "PRHOTELS DATA:\nHotelName:{}\tRoom Available:{}\tLocation:{}\tRating:{}\tPriceper Room:{}".format(
            self.name, self.roomAvl, self.location, self.rating, self.pricePr)

    class User:
        def __init__(self):
            self.uname = ''
            self.uId = 0
            self.cost = 0

        def __repr__(self):
            return "UserName:{}\tUserId:{}\tBooking Cost:{}".format(self.uname, self.uId, self.cost)

    @classmethod
    def PrintHotelData(cls, hotels):
        for h in hotels:
            print(h)

    @classmethod
    def SortHotelByName(cls, hotels):
        print("SORT BY NAME: ")
        Hotel.sortByName()
        hotels.sort()
        cls.PrintHotelData(hotels)
        print()

    @classmethod
    def SortHotelByRating(cls, hotels):
        print("SORT BY RATING: ")
        Hotel.sortByRate()
        hotels.sort()
        cls.PrintHotelData(hotels)
        print()

    @classmethod
    def PrintHotelByCity(cls, city, hotels):
        print("HOTELS FOR {} LOCATION ARE:".format(city))
        hotelsByLoc = [h for h in hotels if h.location == city]
        cls.PrintHotelData(hotelsByLoc)
        print()

    @classmethod
    def SortByRoomAvailable(cls, hotels):
        print("SORT BY ROOM AVAILABLE: ")
        cls.sortByRoomAvailable()
        hotels.sort()
        cls.PrintHotelData(hotels)
        print()

    @classmethod
    def PrintUserData(cls, users, hotels):
        for user, hotel in zip(users, hotels):
            print(user, "\tHotel Name:", hotel.name)

    @classmethod
    def HotelManagement(cls, user_names, user_ids, hotel_names, booking_costs, rooms, locations, ratings, prices):
        hotels = []

        for i in range(3):
            h = Hotel()
            h.name = hotel_names[i]
            h.roomAvl = rooms[i]
            h.location = locations[i]
            h.rating = ratings[i]
            h.pricePr = prices[i]
            hotels.append(h)

        users = [Hotel.User() for i in range(len(user_names))]

        for i, user in enumerate(users):
            user.uname = user_names[i]
            user.uId = user_ids[i]
            user.cost = booking_costs[i]

        print("Hotel Data:")
        cls.PrintHotelData(hotels)
        cls.SortHotelByName(hotels)
        cls.SortHotelByRating(hotels)
        cls.PrintHotelByCity("Bangalore", hotels)
        cls.SortByRoomAvailable(hotels)
        print("User Data:")
        cls.PrintUserData(users, hotels)

if __name__ == '__main__':
    user_names = ["U1", "U2", "U3"]
    user_ids = [2, 3, 4]
    hotel_names = ["H1", "H2", "H3"]
    booking_costs = [1000, 1200, 1100]
    rooms = [4, 5, 6]
    locations = ["Bangalore", "Bangalore", "Mumbai"]
    ratings = [5, 5, 3]
    prices = [100, 200, 100]

    Hotel.HotelManagement(user_names, user_ids, hotel_names, booking_costs, rooms, locations, ratings, prices)
