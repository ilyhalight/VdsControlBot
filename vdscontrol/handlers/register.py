from handlers import \
    stats_handler, \
    on_start_handler, \
    cancel_handler, \
    add_vds_handler, \
    remove_vds_handler


def register_handlers(dp):
    stats_handler.setup(dp)
    on_start_handler.setup(dp)
    cancel_handler.setup(dp)
    add_vds_handler.setup(dp)
    remove_vds_handler.setup(dp)
