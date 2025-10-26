from .packager import package_files

def format_files(scripture_data):
  print(f'[Formatter] Formatting files with spec: {scripture_data}.')

  # Generate files for packaging
  gen_files = ['placeholder1', 'placeholder2', 'placeholder3']

  # Package files
  return package_files(gen_files)
