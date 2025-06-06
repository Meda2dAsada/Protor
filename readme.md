To enable this feature on Windows, you need to modify the registry:

1. Open the Registry Editor (`regedit`).
2. Navigate to the following path:
   HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\FileSystem
3. Locate the corresponding entry (e.g., "LongPathsEnabled" or another relevant key).
4. Set its value from 0 to 1 (hexadecimal) to enable the feature.

**Warning:** Editing the Windows Registry can affect system stability. Proceed with caution and consider backing up the registry before making any changes.
