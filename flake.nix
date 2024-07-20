{
  description = "stats devshell";

  outputs =
    { self, nixpkgs }:
    let
      forAllSystems =
        f:
        nixpkgs.lib.genAttrs [
          "x86_64-linux"
          "aarch64-darwin"
        ] (system: f nixpkgs.legacyPackages.${system});
    in
    {
      formatter = forAllSystems (pkgs: pkgs.alejandra);
      devShells = forAllSystems (
        pkgs:
        let
          python-with-pkgs = pkgs.python3.withPackages (
            ps: with ps; [
              polars
              numpy
              scipy
              seaborn
            ]
          );
        in
        {
          default = pkgs.mkShell {
            name = "stats";
            packages = with pkgs; [
              python-with-pkgs
              gcc
              gmpxx
            ];
          };
        }
      );
    };
}
