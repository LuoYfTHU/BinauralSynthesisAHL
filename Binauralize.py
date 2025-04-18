import pyfar as pf
from IPython.display import Audio, display


def BinauralAudioFromHRIR(elevation, azimuth, radius, hrirs, sources):
    
    # Get castanets example audio
    castanets = pf.signals.files.castanets()

    desired_direction = pf.Coordinates.from_spherical_elevation(
        azimuth, elevation, radius
    )

    index, _ = sources.find_nearest(desired_direction)

    #sources.show(index)

    # find the desired source position
    desired_direction = pf.Coordinates.from_spherical_elevation(
        azimuth, elevation, radius)
    index, _ = sources.find_nearest(desired_direction)

    # Generate binaural version by convolution with the HRIRs
    binaural_audio = pf.dsp.convolve(castanets, hrirs[index])

    # render the binaural audio
    player_binaural = Audio(binaural_audio.time, rate=binaural_audio.sampling_rate)
    display(player_binaural)

    return