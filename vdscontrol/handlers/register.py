from handlers import \
    info_handler, \
    on_start_handler, \
    cancel_handler, \
    add_vds_handler, \
    remove_vds_handler, \
    list_handler


def register_handlers(dp):
    info_handler.setup(dp)
    on_start_handler.setup(dp)
    cancel_handler.setup(dp)
    add_vds_handler.setup(dp)
    remove_vds_handler.setup(dp)
    list_handler.setup(dp)
