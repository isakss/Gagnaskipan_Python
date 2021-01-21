""" A series of practice programs that are aimed at testing certain classes and functions """

import unittest

class PizzaCollection:
    def __init__(self):
        self._served = {}
        self._unserved = {}
        self._id = 1

    def add_pizza(self, toppings):
        self._unserved[self._id] = toppings
        self._id += 1
    
    def serve_pizza(self, id):
        try:
            self._served[id] = self._unserved[id].copy()
            del self._unserved[id]
        except KeyError:
            "Pizza does not exist or is already served."

    def print_pizzas(self):
        served_string = "{}\n{}\n".format("Served Pizzas: ", self._served)
        unserved_string = "{}\n{}\n".format("Unserved Pizzas: ", self._unserved)

        return served_string + unserved_string

    def remove_all_served(self):
        self._served.clear()

class StreetNeighbourhoodCollection:
    def __init__(self):
        self._neighbourhood_dict = {}

    def add_street(self, neighbourhood_string, street_string):
        if neighbourhood_string not in self._neighbourhood_dict:
            self._neighbourhood_dict[neighbourhood_string] = [street_string]
        else:
            self._neighbourhood_dict[neighbourhood_string].append(street_string)

    def print_streets(self, key_string):
        pass
        

class TestPizzaCollectionMethods(unittest.TestCase):
    def test_pizza(self):
        pc = PizzaCollection()

        pc.add_pizza(["skinka", "sveppir"])
        self.assertEqual(len(pc._unserved), 1)
        pc.add_pizza(["skinka", "ananas"])
        self.assertEqual(len(pc._unserved), 2)

        pc.serve_pizza(2)
        self.assertEqual(len(pc._unserved), 1)
        self.assertEqual(len(pc._served), 1)
        self.assertTrue("sveppir" in pc._unserved[1])

        pizza_string = pc.print_pizzas()
        print(pizza_string)
        
        pc.remove_all_served()
        self.assertEqual(len(pc._served), 0)

class TestNeighbourhoodStreet(unittest.TestCase):
    def test_neigbourhood(self):
        ns = StreetNeighbourhoodCollection()

        ns.add_street("midtown","willywonka st.")
        self.assertEqual(len(ns._neighbourhood_dict), 1)
        ns.add_street("midtown", "rowdy blvd.")
        self.assertEqual(len(ns._neighbourhood_dict["midtown"]), 2)
        ns.add_street("Uritheru", "Deep Market")
        self.assertEqual(len(ns._neighbourhood_dict), 2)



if __name__ == "__main__":
    unittest.main()
    