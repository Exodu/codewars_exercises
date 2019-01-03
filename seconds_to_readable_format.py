# Your task in order to complete this Kata is to write a function which formats a duration, given as a number of seconds, in a human-friendly way.

# The function must accept a non-negative integer. If it is zero, it just returns "now". Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.


# Example: format_duration(676324) - > 7 days, 19 hours, 52 minutes and 4 seconds
# Example: format_duration(888) - > 14 minutes and 48 seconds

times = [("year", 365 * 24 * 60 * 60),
         ("day", 24 * 60 * 60),
         ("hour", 60 * 60),
         ("minute", 60),
         ("second", 1), ]


def format_duration(seconds):
    if not seconds:
        return 'now'

    chunks = []
    for name, duration in times:
        value = seconds // duration
        if value:
            if value > 1:
                name += "s"
            chunks.append(str(value) + " " + name)

        seconds = seconds % duration
    print(chunks[:-1])

    return ', '.join(chunks[:-1]) + ' and ' + chunks[-1] if len(chunks) > 1 else chunks[0]
