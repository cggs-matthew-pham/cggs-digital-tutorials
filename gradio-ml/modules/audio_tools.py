import tensorflow as tf


DEFAULT_SAMPLE_RATE = 16000
DEFAULT_SECONDS = 1.0


def waveform_to_spectrogram(waveform):
    """
    Convert audio waveform data into a spectrogram.
    """

    spectrogram = tf.signal.stft(
        waveform,
        frame_length=255,
        frame_step=128
    )

    spectrogram = tf.abs(spectrogram)

    # Add a channel dimension so it behaves like an image
    spectrogram = spectrogram[..., tf.newaxis]

    return spectrogram


def _audio_batch_to_spectrogram(audio, label):
    """
    Convert a batch of audio into spectrograms.
    """

    # Convert stereo/multi-channel audio to mono
    audio = tf.reduce_mean(audio, axis=-1)

    spectrogram = waveform_to_spectrogram(audio)

    return spectrogram, label


def prepare_audio_dataset(dataset):
    """
    Convert an audio dataset into a spectrogram dataset.
    """

    dataset = dataset.map(
        _audio_batch_to_spectrogram,
        num_parallel_calls=tf.data.AUTOTUNE
    )

    return dataset.prefetch(tf.data.AUTOTUNE)


def load_wav(
    filename,
    sample_rate=DEFAULT_SAMPLE_RATE,
    seconds=DEFAULT_SECONDS
):
    """
    Load one WAV file ready for prediction.
    """

    audio_binary = tf.io.read_file(filename)

    waveform, actual_sample_rate = tf.audio.decode_wav(
        audio_binary,
        desired_channels=1
    )

    actual_sample_rate = int(actual_sample_rate.numpy())

    if actual_sample_rate != sample_rate:
        raise ValueError(
            f"Audio must be {sample_rate} Hz. "
            f"This file is {actual_sample_rate} Hz."
        )

    waveform = tf.squeeze(waveform, axis=-1)

    required_length = int(sample_rate * seconds)

    # Cut long files
    waveform = waveform[:required_length]

    # Pad short files with silence
    missing = required_length - tf.shape(waveform)[0]

    waveform = tf.pad(
        waveform,
        [[0, tf.maximum(missing, 0)]]
    )

    return waveform