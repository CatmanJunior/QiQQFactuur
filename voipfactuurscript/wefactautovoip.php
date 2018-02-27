<?php

require_once("../wefact_api.php");

$api = new WeFactAPI();

$invoiceParams = array(
				'DebtorCode'	=> 'DB0001',	// Customer information will automatically be fetched

				'InvoiceLines'	=> array(
					array(
						'Description'	=> 'Setupfee',
						'PriceExcl'		=> 150
					),
					array(
						'ProductCode'	=> 'P003',
						'Description'	=> 'Domain example.com'
					)
				)
);

$response = $api->sendRequest('invoice', 'add', $invoiceParams);

print_r_pre($response);

?>