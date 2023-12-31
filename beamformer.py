{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyO4lcOGbykD/1x6VCBmG3HA",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/iimahdii/-beam-steering-beamformer-/blob/main/Beam-Steering-Beamfoermer.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "N2CaodVfJR2k"
      },
      "outputs": [],
      "source": [
        "import numpy as np\n",
        "\n",
        "def generate_signal(frequency, duration, sample_rate):\n",
        "    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)\n",
        "    signal = np.sin(2 * np.pi * frequency * t)\n",
        "    return signal\n",
        "\n",
        "def beamformer(array_positions, steering_angle, signal, sample_rate):\n",
        "    num_mics = len(array_positions)\n",
        "    num_samples = len(signal)\n",
        "    delays = np.zeros(num_mics)\n",
        "\n",
        "    for mic_idx, mic_position in enumerate(array_positions):\n",
        "        distance = np.linalg.norm(mic_position)\n",
        "        time_delay = distance * np.sin(np.radians(steering_angle)) / 343.0\n",
        "        sample_delay = int(round(time_delay * sample_rate))\n",
        "        delays[mic_idx] = sample_delay\n",
        "\n",
        "    output = np.zeros(num_samples - max(delays))\n",
        "    for mic_idx, delay in enumerate(delays):\n",
        "        output += signal[delay:delay + len(output)]\n",
        "\n",
        "    return output\n",
        "\n",
        "# Parameters\n",
        "frequency = 1000  # Hz\n",
        "duration = 1.0   # seconds\n",
        "sample_rate = 44100  # samples per second\n",
        "steering_angle = 30  # degrees\n",
        "\n",
        "# Generate signal\n",
        "signal = generate_signal(frequency, duration, sample_rate)\n",
        "\n",
        "# Define microphone positions (simplified 2D positions)\n",
        "array_positions = [\n",
        "    np.array([0.0, 0.0]),\n",
        "    np.array([0.1, 0.0]),\n",
        "    np.array([0.2, 0.0]),\n",
        "]\n",
        "\n",
        "# Apply beamforming\n",
        "beamformed_signal = beamformer(array_positions, steering_angle, signal, sample_rate)\n",
        "\n",
        "# You can now analyze or play the beamformed_signal\n"
      ]
    }
  ]
}
