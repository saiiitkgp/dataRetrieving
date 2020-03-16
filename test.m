
data=load('Merged_20180201T230002_20180228T073405_log.mat');

variable_name= "C'Geb1951'00'PwrActv"
raw_data = data.DataContainer();


bacnet_names = raw_data(:,2);
row_index = find(strcmp(variable_name, bacnet_names));
%values = cell2mat(raw_data(row_index,4));
data_values = (raw_data(row_index,4));
data_values = data_values{1};
type_values = data_values(1:1);

if (isfloat(type_values))
    values = data_values;
elseif (iscell(type_values))
    ReplaceIdx = find(strcmp(data_values, 'active'));
    values(ReplaceIdx,1) = 10;
    ReplaceIdx = find(strcmp(data_values, 'inactive'));
    values(ReplaceIdx,1) = 0;
end


if isempty(values) == 1
    disp (raw_data);
    error(strcat(variable_name, '  - BACnet value not found!'));
end
