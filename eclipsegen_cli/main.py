from eclipsegen_cli.cmd import EclipseGeneratorCLI


def main():
  try:
    EclipseGeneratorCLI.run()
  except KeyboardInterrupt as ex:
    print(ex)
