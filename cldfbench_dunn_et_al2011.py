import pathlib

import phlorest


class Dataset(phlorest.Dataset):
    dir = pathlib.Path(__file__).parent
    id = "dunn_et_al2011"

    def cmd_makecldf(self, args):
        self.init(args)
        args.writer.add_summary(
            self.raw_dir.read_tree(
                'utoaztecan.mcct.trees',
                detranslate=True),
            self.metadata,
            args.log)
        posterior = self.sample(
            self.raw_dir.read('utoaztecan-postburnin.trees.gz'),
            n=800,
            detranslate=True,
            as_nexus=True)
        args.writer.add_posterior(
            posterior.trees.trees,
            self.metadata,
            args.log)
        args.writer.add_data(
            self.raw_dir.read_nexus('utoaztecan.nex'),
            self.characters,
            args.log)

