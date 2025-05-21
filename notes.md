## work on slides feature

- I need to able to set a theme
- to_json is broken

### how to customize a theme

- currently we import a theme module that provides apis to Doc (head, doc), Code (code) and Image (image) blocks
- an option could be to add a way for the module to update the api (a theme.set("slides"))
- this could be done with or without changing the Doc object
- reference to change for a slides theme: https://github.com/HugoGranstrom/nimiSlides/blob/main/src/nimiSlides.nim
- two options I see now:
  - either I add a theme object to block hierarchy (and a parent relationship to get theme from parent)
  - or I use a global theme object
- maybe for the moment it is simpler the second option
- but maybe it does not work, current implementation fails with 
`AttributeError: 'Theme' object has no attribute 'slide'`
so the global object was not recognized (I though it was a pydantic)
- understood the problem! it is `import nobe; nobe.theme = ...` and not `from nobe import theme; theme = ...`

I am stuck

## Publishing the package

### renaming to nobe

- renaming in repo [x]
- publishing with new name [x]
- renaming the repo [x]
- remove mib from pypi [x]

### OSS Turin - March 15

- uv init with hatch as build backend [x]
    - test uv setup with `uv run python -c "import mib"` [x]
- link with repo on github
- add MIT license
- build and publish on testpypi
    - create account on testpypi (and verify mail) [x]
    - 2fa authentication needed (used also authenticator) [x]
    - publish with username and passwrod not allowed, needs token [x]
    - get API token [x]
    - need to use `uv publish --index=testpypi`
    - name too similar to existing project
- project name mib change to mib-notebook [x]
  - need to tell hatchling about where to find new name [x]
- publish on testpypi [x]
  - publish ok [x]
  - test install [x]
    `uv run --index=testpypi --with mib-notebook --no-project -- python -c "import mib"`
🥳 yes, publish on testpypi works!


- add some minimally interesting code [x]
- build and publish on pypi and test with [x]
- test with [x]
   uv run --with mib-notebook --no-project -- python -c "import mib"
   uv run --with mib-notebook --no-project -- python example.py
- minimal project info required (license, readme, classifier) [x]
- learn that to publish again I need to bump the version! [x]

### basic code with pydantic

serializing a list of pydantic base models is non trivial with pydantic:
https://github.com/pydantic/pydantic/issues/675

### weird error after renaming

since mib was not an allowed name (not on test pypi), I was trying mib-notebook
then uv build stopped working with this error message and does not work again after changing name
this is due to somehow uv build now checking on test index instead of standard index.


```
Building source distribution...
× Failed to build `/Users/pietropeterlongo/recursing/mib`
  ├─▶ Failed to resolve requirements from `build-system.requires`
  ├─▶ No solution found when resolving: `hatchling`
  ╰─▶ Because only packaging==16.7 is available and hatchling<=0.19.0 depends on packaging>=21.3,<22.dev0, we can conclude that hatchling<=0.19.0 cannot be used.
      And because only the following versions of hatchling are available:
          hatchling==0.8.0
          hatchling==0.8.1
          hatchling==0.8.2
          hatchling==0.9.0
          hatchling==0.10.0
          hatchling==0.11.0
          hatchling==0.11.1
          hatchling==0.11.2
          hatchling==0.11.3
          hatchling==0.12.0
          hatchling==0.13.0
          hatchling==0.14.0
          hatchling==0.15.0
          hatchling==0.16.0
          hatchling==0.17.0
          hatchling==0.18.0
          hatchling==0.19.0
          hatchling==0.20.0
          hatchling==0.20.1
          hatchling==0.21.0
          hatchling==0.21.1
          hatchling==0.22.0
          hatchling==0.23.0
          hatchling==0.24.0
          hatchling==0.25.0
          hatchling==0.25.1
          hatchling==1.0.0
          hatchling==1.1.0
          hatchling==1.2.0
          hatchling==1.3.0
          hatchling==1.3.1
          hatchling==1.4.0
          hatchling==1.4.1
          hatchling==1.5.0
          hatchling==1.6.0
          hatchling==1.7.0
          hatchling==1.7.1
          hatchling==1.8.0
          hatchling==1.8.1
          hatchling==1.9.0
          hatchling==1.10.0
          hatchling==1.11.0
          hatchling==1.11.1
          hatchling==1.12.0
          hatchling==1.12.1
          hatchling==1.12.2
          hatchling==1.13.0
          hatchling==1.14.0
          hatchling==1.14.1
          hatchling==1.15.0
          hatchling==1.16.0
          hatchling==1.16.1
          hatchling==1.17.0
          hatchling==1.17.1
          hatchling==1.18.0
          hatchling==1.19.0
          hatchling==1.19.1
          hatchling==1.20.0
          hatchling==1.21.0
          hatchling==1.21.1
          hatchling==1.22.0
          hatchling==1.22.1
          hatchling==1.22.2
          hatchling==1.22.3
          hatchling==1.22.4
          hatchling==1.22.5
          hatchling==1.23.0
          hatchling==1.24.0
          hatchling==1.24.1
          hatchling==1.24.2
          hatchling==1.25.0
          hatchling==1.26.0
          hatchling==1.26.1
          hatchling==1.26.2
          hatchling==1.26.3
          hatchling==1.27.0
      we can conclude that hatchling<0.20.0 cannot be used. (1)

      Because only packaging==16.7 is available and hatchling>=0.20.0,<=0.25.1 depends on packaging>=21.3, we can conclude that hatchling>=0.20.0,<=0.25.1 cannot
      be used.
      And because we know from (1) that hatchling<0.20.0 cannot be used, we can conclude that hatchling<1.0.0 cannot be used. (2)

      Because only packaging==16.7 is available and all of:
          hatchling>=1.0.0,<=1.3.1
          hatchling>=1.4.1,<=1.19.0
          hatchling>=1.20.0,<=1.21.1
          hatchling>=1.22.2,<=1.22.5
      depend on packaging>=21.3, we can conclude that all of:
          hatchling>=1.0.0,<=1.3.1
          hatchling>=1.4.1,<=1.19.0
          hatchling>=1.20.0,<=1.21.1
          hatchling>=1.22.2,<=1.22.5
       cannot be used.
      And because we know from (2) that hatchling<1.0.0 cannot be used, we can conclude that all of:
          hatchling<1.4.0
          hatchling>1.4.0,<1.19.1
          hatchling>1.19.1,<1.22.0
          hatchling>1.22.1,<1.23.0
       cannot be used.
      And because hatchling==1.4.0 was yanked (reason: Building wheels from sdists is broken), we can conclude that all of:
          hatchling<1.19.1
          hatchling>1.19.1,<1.22.0
          hatchling>1.22.1,<1.23.0
       cannot be used.
      And because hatchling==1.19.1 was yanked (reason: https://github.com/pypa/hatch/issues/1129) and hatchling>=1.22.0,<=1.22.1 was yanked (reason: Broken
      builds from sdists), we can conclude that hatchling>=1.22.0,<=1.22.1 cannot be used. (3)

      Because only packaging==16.7 is available and hatchling>=1.23.0,<=1.25.0 depends on packaging>=23.2, we can conclude that hatchling>=1.23.0,<=1.25.0 cannot
      be used.
      And because we know from (3) that hatchling>=1.22.0,<=1.22.1 cannot be used, we can conclude that hatchling<1.26.0 cannot be used.
      And because hatchling==1.26.0 was yanked (reason: Incompatible with currently released Hatch) and hatchling>=1.26.1,<=1.26.2 was yanked (reason: Upload
      issues), we can conclude that hatchling>=1.26.1,<=1.26.2 cannot be used. (4)

      Because only packaging==16.7 is available and hatchling>=1.26.3 depends on packaging>=24.2, we can conclude that hatchling>=1.26.3 cannot be used.
      And because we know from (4) that hatchling>=1.26.1,<=1.26.2 cannot be used, we can conclude that all versions of hatchling cannot be used.
      And because you require hatchling, we can conclude that your requirements are unsatisfiable.

      hint: `packaging` was found on https://test.pypi.org/simple/, but not at the requested version (packaging>=21.3). A compatible version may be available on
      a subsequent index (e.g., https://pypi.org/simple). By default, uv will only consider versions that are published on the first index that contains a given
      package, to avoid dependency confusion attacks. If all indexes are equally trusted, use `--index-strategy unsafe-best-match` to consider all versions from
      all indexes, regardless of the order in which they were defined.
      ```