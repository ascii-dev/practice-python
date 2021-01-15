"""Data Structures & Algorithms in Python: Goodrich, Tamassia & Goldwasser"""
import ctypes  # provides low level arrays

class DynamicArray:
    """A dynamic array class akin to a simplified Python list"""

    def __init__(self):
        """Creates an empty array"""
        self._n = 0  # count actual element
        self._capacity = 1  # default array capacity
        self._array = self._make_array(self._capacity)  # low-level array

    def __len__(self):
        """Return number of elements stored in the array"""
        return self._n

    def __getitem__(self, k):
        """Return element at index k"""
        if not 0 <= k <= self._n:
            raise IndexError('Invalid index')
        return self._array[k]  # retrieve from array

    def apend(self, obj):
        """Add object to end of array"""
        if self._n == self._capacity:  # not enough room
            self._resice(2 * self._capacty)  # so double capacity
        self._array[self._n] = obj
        self._n += 1

    def _resize(self, c):
        """Resize internal array to capaccity c"""
        new_array = self._make_array(c)  # new bigger array
        for k in range(self._n):  # for each existing value
            new_array[k] = self._array[k]
        self._array = new_array  # use the bigger array
        self._capacity = c

    def _make_array(self, c):
        """Return new array with capacity c"""
        return (c * ctypes.py_object)()  # ctypes documentation
