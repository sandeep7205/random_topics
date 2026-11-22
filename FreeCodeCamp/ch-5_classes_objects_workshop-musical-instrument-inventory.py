
class MusicalInstrument:
    """
    Represents a musical instrument with a name and instrument type.
    Provides methods to play the instrument and get information about it.
    """

    def __init__(self, name, instrument_type):
        """Initialize a musical instrument with its name and type."""

        self.name = name                  # Store the instrument's name
        self.instrument_type = instrument_type  # Store its instrument family

    def play(self):
        """Display a message saying that the instrument is fun to play."""

        print(f'The {self.name} is fun to play!')

    def get_fact(self):
        """Return information about the instrument and its family."""

        return f'The {self.name} is part of the {self.instrument_type} family of instruments.'


# Create the first musical instrument object
instrument_1 = MusicalInstrument('Oboe', 'woodwind')

# Create the second musical instrument object
instrument_2 = MusicalInstrument('Trumpet', 'brass')


# Play the first instrument
instrument_1.play()

# Display information about the first instrument
print(instrument_1.get_fact())


# Play the second instrument
instrument_2.play()

# Display information about the second instrument
print(instrument_2.get_fact())
