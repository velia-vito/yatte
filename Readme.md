<!-- rumdl-disable-file MD036-->

<!-- rumdl-disable-next-line MD033 -->
<h1> <ins>Y</ins>et <ins>A</ins>nother <ins>T</ins>ex<ins>T</ins> <ins>E</ins>ditor </h1>

__*Yatte is meant to be a simple, flexible, single-app solution to documenting, drafting, and revising
your writing projects.*__

## Technical Targets

__General__

- [ ] Below 10ms keyboard-to-screen latency for all tasks.
- [ ] Multi-platform.
- [ ] Cross-device Sync.

__Documentation__

- [ ] Simple cross-file / cross-section linking.
- [ ] Support for merging cells in markdown tables.
- [ ] Support for front/back links.
- [ ] Queriable YAML based Metadata.

__Drafting__

- [ ] Contiguous file viewing (like in Scrivener3)
- [ ] Multiplexed Workspace views.
- [ ] Revision tracking.
- [ ] First class support for `.docx` format.
  - [ ] Export to `.docx`
  - [ ] Import `.docx` including tracked changes & comment-threads.

__Unconfirmed Additions__

- [ ] Plug-in based extensibility.

## Repository Management

As you might have noticed, the `yatte_app`, `yatte_component_editor`, etc aren't quite folders within
the repository but rather links to other repositiories. This leads to slight complications during
repository cloning and updating this repository.

### Cloning / Pulling

1. Clone the Repository.

   ```sh
   git clone https://github.com/velia-vito/yatte.git
   ```

2. Initialize Submodules

   ```sh
   yatte$ git submodule init
   ```

3. Update Submodules to the recommended commits. This may not be latest commit on each Submodule.

   ```sh
   yatte$ git submodule update
   ```

   Or, update each Submodule to the latest commit. This is guarenteed to be the latest commit on each
   Submodule, the code may break due to version inconsistencies.

   ```sh
   yatte$ git pull --recurse-submodules
   ```

### Pushing

1. Commit Changes within the Submodule folder.

   ```sh
   yatte/yatte_app$ git add .
   ```

   ```sh
   yatte/yatte_app$ git commit -m "New Commit In Submodule"
   ```

2. Push Changes within Submodule folder. This ensures that when others try to pull this updated commit
from the remote repository, the commit being referenced actually exists on the remote.

   ```sh
   yatte/yatte_app$ git push
   ```

3. Commit changes from the Super Project folder. This doesn't commit the files in the Submodules, it
merely updates the specific commit being referenced in the Submodule listing.

   ```sh
   yatte$ git add yatte_app
   ```

   ```sh
   yatte$ git commit -m "Updating SubModule Commit Ref"
   ```

4. Push Changes from the Super Project folder.

   ```sh
   yatte$ git push
   ```
