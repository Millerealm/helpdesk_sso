def get_dashboard_data(data):
	data.setdefault("non_standard_fieldnames", {})["Task"] = "custom_hd_ticket"
	data.setdefault("transactions", []).append(
		{
			"label": "Internal",
			"items": ["Task"],
		}
	)
	return data
