# CHANGELOG

## 1.2.1 (2022.07.22)

### ENHANCEMENTS

- Reconfigured gitlab runner configuration
- Enabled deploy to production
- Updated Azure Pipeline (I have no way to test if this works right now.)

## 1.2.0 (2022.07.21)

### ENHANCEMENTS

- Added the ability to import external translators

## 1.1.2 (2022.05.26)

### BUG FIX

- Changed os.rename to os.replace (windows doesn't like os.rename)
- Validate path now checks that basepaths exist before trying to create directories.

## 1.1.1 (2022.05.22)

### BUG FIX

- Added version flag to click methods
- Fixed typo in github flow

## 1.1.0 (2022.05.22)

### ENHANCEMENTS

- Updated gitlab-ci to use docker
- Updated github workflows to use new template
- Mirrored gitlab repository with github

## 1.0.0 (2022.05.22)

- Program Released

## 0.1.0 (2022.05.21)

- Program Created
