# Environment

## Aims
* isolate environments of different projets with different dependencies
    * + system Python can be left alone (less chance to screw your system up)
    * + different versions of the same lib can be used in parallel
    * - Technical overhead to get set up
    * - Mental overhead switching between projects
    
* downside if virtualenv: missing system package dependencies


System wide:

Easy: Vagrant
Advanced: Docker
Rocket Science: nix
