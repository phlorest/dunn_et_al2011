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
        # no burn-in to remove
        posterior = self.raw_dir.read_trees(
            'utoaztecan-postburnin.trees.gz', detranslate=True)
        args.writer.add_posterior(
            posterior,
            self.metadata,
            args.log)
        args.writer.add_data(
            self.raw_dir.read_nexus('utoaztecan.nex'),
            self.characters,
            args.log)
