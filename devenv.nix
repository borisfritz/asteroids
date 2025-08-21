# devenv.nix
{ pkgs, ... }:

{
  # Setup a Python + uv environment
  languages.python = {
    enable = true;
    package = pkgs.python3;
    uv.enable = true;
  };

  # Packages required to run pygame under Wayland (Hyprland)
  packages = with pkgs; [
    # Runtime dependencies for SDL/pygame
    SDL2
    SDL2_image
    SDL2_mixer
    SDL2_ttf
    alsa-lib
    libpulseaudio
    libGL
    mesa
    wayland
    xorg.libX11
    xorg.libXcursor
    xorg.libXrandr
    xorg.libXinerama
    xorg.libXi
    dbus
    libxkbcommon
  ];

  # Environment variables for SDL and Wayland
  env = {
    # Explicitly set SDL to use Wayland
    SDL_VIDEODRIVER = "wayland";  # or try "x11" if wayland fails
    XDG_RUNTIME_DIR = "/run/user/1000";  # adjust if necessary
  };

  scripts.runGame.exec = "python main.py";
}

